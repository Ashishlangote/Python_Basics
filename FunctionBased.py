from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404


@api_view(http_method_names=["GET", "POST"])
def posts_list(request: Request):
    all_posts = Post.objects.all()
    serializer = PostSerializer(instance=all_posts, many=True)
    response = {
        "message": "All data received",
        "data": serializer.data
    }
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def post_detail(request: Request, id: int):
    post = get_object_or_404(Post, pk=id)
    serializer = PostSerializer(instance=post)
    if post:
        response = {
            "message": f"Post detail for id {id} fetched successfully",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=['POST'])
def post_create(request: Request):

    if request.method == 'POST':
        data = request.data
        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "Post created successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["PUT"])
def post_update(request: Request, id: int):

    post = get_object_or_404(Post, pk=id)
    data = request.data
    serializer = PostSerializer(instance=post, data=data)

    if serializer.is_valid():
        serializer.save()

        response = {
            "message": f"Post with id {id} updated successfully",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    else:
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["DELETE"])
def post_delete(request: Request, id: int):

    post = get_object_or_404(Post, pk=id)
    post.delete()

    response = {
        "message": f"Post wiht id {id} deleted successfully"
    }
    return Response(data=response, status=status.HTTP_200_OK)



# Urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.posts_list, name="posts-list"),
    path("<int:id>", views.post_detail, name="posts-detail"),
    path("create/", views.post_create, name="post-create"),
    path("update/<int:id>", views.post_update, name="post-update"),
    path("delete/<int:id>", views.post_delete, name="post-delete"),
]


# ==========================================================================================
# Class based
class PostsList(APIView):

    def get(self, request: Request, *args, **kwargs):
        posts = Post.objects.all()

        serializer = PostSerializer(instance=posts, many=True)

        response = {
            "message": "List posts fetched successfully",
            "data": serializer.data
        }

        return Response(data=response, status=status.HTTP_200_OK)


class PostCreate(APIView):

    def post(self, request: Request, *args, **kwargs):
        data = request.data
        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "Post created successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostUpdate(APIView):

    def put(self, request: Request, id: int, *args, **kwargs):

        post = get_object_or_404(Post, pk=id)
        data = request.data
        serializer = PostSerializer(instance=post, data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": f"Post with id {id} updated successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDelete(APIView):

    def delete(self, request: Request, id: int, *args, **kwargs):
        post = get_object_or_404(Post, pk=id)
        post.delete()

        response = {
            "message": f"Post wiht id {id} deleted successfully"
        }
        return Response(data=response, status=status.HTTP_200_OK)


# Session and query string


# =========================================================================================
# Model Mixin
class PostListView(generics.GenericAPIView, mixins.ListModelMixin):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostCreateView(generics.GenericAPIView, mixins.CreateModelMixin):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def post(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {"message": f"The post has been successfully created",
                    "data": serializer.data
                    }
        return Response(response, status=status.HTTP_201_CREATED)

    # def post(self, request:Request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class PostDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        id = instance.id
        response = {"message": f"The data is fecthed {id}.",
                    "data": serializer.data
                    }
        return Response(response, status=status.HTTP_200_OK)

    # def get(self, request:Request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)


class PostUpdateView(generics.GenericAPIView, mixins.UpdateModelMixin):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def put(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        id = instance.id
        self.perform_update(instance)
        response = {"message": f"The post has been successfully updated {id}."}
        return Response(response, status=status.HTTP_200_OK)

    # def put(self, request:Request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)


class PostDeleteView(generics.GenericAPIView, mixins.DestroyModelMixin):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # def delete(self, request:Request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        response = {"message": "The post has been successfully deleted."}
        return Response(response, status=status.HTTP_204_NO_CONTENT)


# =========================================================================================
# Viewsets

class PostsViewset(viewsets.ViewSet):
    def list(self, request: Request):
        all_post = Post.objects.all()
        serializer = PostSerializer(instance=all_post, many=True)
        response = {
            "message": "Hello from DRF",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)

    def retrieve(self, request: Request, pk: int):
        all_post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(instance=all_post)
        if all_post:
            response = {
                "message": f"Post detail for id {pk} fetched successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)

    def create(self, request: Request):
        if request.method == 'POST':
            data = request.data
            serializer = PostSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

                response = {
                    "message": "Post created successfully",
                    "data": serializer.data
                }
                return Response(data=response, status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request: Request, pk: int):

        post = get_object_or_404(Post, pk=pk)
        data = request.data
        serializer = PostSerializer(instance=post, data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": f"Post with id {pk} updated successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: Request, pk: int):

        post = get_object_or_404(Post, pk=pk)
        post.delete()

        response = {
            "message": f"Post wiht id {pk} deleted successfully"
        }
        return Response(data=response, status=status.HTTP_200_OK)
