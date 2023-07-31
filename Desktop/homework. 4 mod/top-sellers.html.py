{% extends 'base.html' %}
{% load static %}

{% block title %}
Топ продавцов
{% endblock %}

{% block content %}
  <ul class="nav nav-pills sticky-top bg-white nav-fill">
    <li class="nav-item">
      <a class="nav-link"  href="{% url 'main_page' %}">
        <span style="font-weight: bold;">Главная</span>
      </a>
    </li>
    <li class="nav-item">
      <a class="nav-link active" aria-current="page" href="{% url 'top-sellers' %}" ><span style="font-weight: bold;">Топ продавцов</span>
      </a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="advertisement-post.html">
        <span style="font-weight: bold;">Разместить объявление</span>
      </a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="register.html">
        <span style="font-weight: bold;">Регистрация</span>
      </a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="login.html">
        <span style="font-weight: bold;">Войти</span>
      </a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="profile.html">
        <span style="font-weight: bold;">Профиль</span>
      </a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">
        <span style="font-weight: bold;">Выйти</span>
      </a>
    </li>
  </ul>
  <div class="row">
    <div class="col" style="margin: 50px;">
      <div class="display-2">
        <span class="badge bg-primary">Топ продавцов на сайте</span>
      </div>
    </div>
  </div>
  <div class="container" style="min-height: 452px">
    <ul class="list-group list-group-numbered">

      <li class="list-group-item d-flex justify-content-between align-items-start">
        <div class="ms-2 me-auto">
          <div class="fw-bold">Ваня
          </div>
        </div>
        <span class="badge bg-primary rounded-pill">2</span>
      </li>
      <li class="list-group-item d-flex justify-content-between align-items-start">
        <div class="ms-2 me-auto">
          <div class="fw-bold">Петя
          </div>
        </div>
        <span class="badge bg-primary rounded-pill">3</span>
      </li>
      <li class="list-group-item d-flex justify-content-between align-items-start">
        <div class="ms-2 me-auto">
          <div class="fw-bold">Гоша
          </div>
        </div>
        <span class="badge bg-primary rounded-pill">3</span>
      </li>
    </ul>
  </div>
  <footer style="padding: 100px;" class="bg-primary">
    <nav class="navbar navbar-expand-sm navbar-dark">
      <a class="navbar-brand" href="#">Добавьте</a>
      <button class="navbar-toggler d-lg-none" type="button" data-bs-toggle="collapse"
        data-bs-target="#collapsibleNavId" aria-controls="collapsibleNavId" aria-expanded="false"
        aria-label="Toggle navigation"></button>
      <div class="collapse navbar-collapse" id="collapsibleNavId">
        <ul class="navbar-nav me-auto mt-2 mt-lg-0">
          <li class="nav-item">
            <a class="nav-link active" href="#" aria-current="page">сюда<span
                class="visually-hidden">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">что</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="dropdownId" data-bs-toggle="dropdown" aria-haspopup="true"
              aria-expanded="false">хотите</a>
            <div class="dropdown-menu" aria-labelledby="dropdownId">
              <a class="dropdown-item" href="#">например</a>
              <a class="dropdown-item" href="#">ссылки на социальные сети</a>
            </div>
          </li>
        </ul>
        <form class="d-flex my-2 my-lg-0">
          <input class="form-control me-sm-2" type="text" placeholder="Search">
          <button class="btn btn-outline-light my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
    </nav>
  </footer>
{% endblock %}
