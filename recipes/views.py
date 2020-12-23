from django.shortcuts import render,redirect
from recipes.forms import CreateRecipeForm
from recipes.models import Recipe
from django.views.generic import TemplateView

# Create your views here.

class CreateRecipe(TemplateView):
    form=CreateRecipeForm()
    template_name = "recipes/recipes_create.html"
    context = {}

    def get(self, request, *args, **kwargs):
        form = CreateRecipeForm(initial={"created_by":request.user})
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = CreateRecipeForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listrecipe")

class ListRecipes(TemplateView):
    model=Recipe
    template_name = "recipes/my_recipes.html"
    context={}

    def get_query_set(self,user):
        return self.model.objects.filter(created_by=user)

    def get(self, request, *args, **kwargs):
        created_by=request.user
        self.context["users"]=self.get_query_set(created_by)
        return render(request,self.template_name,self.context)

class RecipeEdit(TemplateView):
    model=Recipe
    template_name = "recipes/recipes_edit.html"
    context={}

    def get_query_set(self,id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        user=self.get_query_set(kwargs.get("pk"))
        form=CreateRecipeForm(initial={"created_by":request.user},instance=user)
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        user = self.get_query_set(kwargs.get("pk"))
        form = CreateRecipeForm(instance=user,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listrecipe")

class RecipeView(TemplateView):
    model=Recipe
    template_name = "recipes/recipe_view.html"
    context={}

    def get_query_set(self,id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        user=self.get_query_set(kwargs.get("pk"))
        self.context["user"]=user
        return render(request,self.template_name,self.context)

class RecipeDelete(TemplateView):
    model=Recipe

    def get_object(self,id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        user=self.get_object(kwargs.get("pk"))
        user.delete()
        return redirect("listrecipe")

class AllRecipes(TemplateView):
    model = Recipe
    template_name = "recipes/all_recipes.html"
    context = {}

    def get_query_set(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        self.context["recipes"]=self.get_query_set()
        return render(request,self.template_name,self.context)





