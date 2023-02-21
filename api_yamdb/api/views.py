from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from reviews.models import Category, Genre, Review, Title
from .mixins import GetListCreateDeleteMixin
from .permissions import IsAdminOrReadOnly, IsAuthorModeratorAdminOrReadOnly
from .registration.confirmation import send_confirmation_code
from .registration.token_generator import get_token_for_user
from .serializers import (
    CommentSerializer,
    GetAuthTokenSerializer,
    ReviewSerializer,
    SignUpSerializer,
    UserProfileSerializer,
    UserSerializer,
)

User = get_user_model()


class UserViewSet(ModelViewSet):
    """Вьюсет модели User."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("username",)
    lookup_field = "username"
    http_method_names = ("get", "post", "delete", "patch")

    @action(
        detail=False,
        methods=["get", "patch"],
        url_path="me",
        url_name="user_profile",
        permission_classes=(IsAuthenticated,),
    )
    def get_patch_self_profile(self, request):
        serializer = UserProfileSerializer(
            request.user, partial=True, data=request.data
        )
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        if request.method == "PATCH":
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class SignUpView(APIView):
    """CBV для регистрации пользователя и получения кода на почту."""

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            email = serializer.validated_data.get("email")
            try:
                user, _ = User.objects.get_or_create(
                    username=username, email=email
                )
                user.confirmation_code = send_confirmation_code(user)
                user.save()
                return Response(
                    serializer.validated_data, status=status.HTTP_200_OK
                )
            except IntegrityError as er:
                return Response(
                    {
                        "error": (
                            "Данное имя пользователя или email "
                            "уже используются"
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAuthTokenView(APIView):
    """CBV для получения и обновления токена."""

    def post(self, request):
        serializer = GetAuthTokenSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        username = serializer.validated_data.get("username")
        confirmation_code = serializer.validated_data.get("confirmation_code")
        user = get_object_or_404(User, username=username)
        if user.confirmation_code != confirmation_code:
            return Response(
                {"confirmation_code": ["Неверный код подтверждения"]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(get_token_for_user(user), status=status.HTTP_200_OK)


class ReviewViewSet(ModelViewSet):
    """
    Получить список всех отзывов.
    Добавление нового отзыва.
    Получение отзыва по id.
    Обновление отзыва по id.
    """

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthorModeratorAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    """
    Получить список всех комментариев.
    Добавление нового комментария к отзыву.
    Получить комментарий по id.
    Обновление комментария по id.
    Удаление комментария.
    """

    serializer_class = CommentSerializer
    permission_classes = (IsAuthorModeratorAdminOrReadOnly,)

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs.get("review_id"))
        return review.comments

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get("review_id"))
        serializer.save(author=self.request.user, review=review)


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет для произведения."""

    queryset = Title.objects.all()
    # serializer_class = TitleSerializer
    permission_classes = [
        IsAdminOrReadOnly,
    ]

    def get_serializer_class(self):
        pass
        # if self.request.method in ('POST', 'PATCH',):
        #     return TitleSerializer
        # return TitleGetSerializer


class CategoryViewSet(GetListCreateDeleteMixin):
    """Вьюсет для категории."""

    queryset = Category.objects.all()
    # serializer_class = CategorySerializer
    permission_classes = [
        IsAdminOrReadOnly,
    ]
    search_fields = (
        "name",
        "slug",
    )
    lookup_field = "slug"


class GenreViewSet(GetListCreateDeleteMixin):
    """Вьюсет для жанра."""

    queryset = Genre.objects.all()
    # serializer_class = GenreSerializer
    permission_classes = [
        IsAdminOrReadOnly,
    ]
    search_fields = ("name", "slug")
    lookup_field = "slug"
