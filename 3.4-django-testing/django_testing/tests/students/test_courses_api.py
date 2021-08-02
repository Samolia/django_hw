import pytest
from django.urls import reverse
from rest_framework import status
from students.models import Course


@pytest.mark.django_db
def test_get_course(api_client, course_factory):
    """проверка получения 1го курса (retrieve-логика)"""
    course_factory(_quantity=7)
    course = Course.objects.first()
    url = reverse('courses-detail', kwargs={'pk': course.id})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == course.name


@pytest.mark.django_db
def test_get_course_list(api_client, course_factory):
    """проверка получения списка курсов (list-логика)"""
    course_factory(_quantity=5)
    url = reverse('courses-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 5


@pytest.mark.django_db
def test_get_course_filtered_by_id(api_client, course_factory):
    """проверка фильтрации списка курсов по id"""
    course_factory(_quantity=7)
    url = '%s?id=3' % reverse('courses-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]['id'] == 3


@pytest.mark.django_db
def test_get_course_filtered_by_name(api_client, course_factory):
    """проверка фильтрации списка курсов по name"""
    Course.objects.bulk_create([
        Course(name='SQL'),
        Course(name='Python'),
        Course(name='C#')
    ])
    url = '%s?name=Python' % reverse('courses-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]['name'] == 'Python'


@pytest.mark.django_db
def test_course_create(api_client):
    """тест успешного создания курса"""
    url = reverse('courses-list')
    data = {'name': 'test'}
    response = api_client.post(url, data=data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'test'


@pytest.mark.django_db
def test_course_update(api_client, course_factory):
    """тест успешного обновления курса"""
    course_factory(name='test')
    course = Course.objects.first()
    data = {'name': 'update_test'}
    url = reverse('courses-detail', kwargs={'pk': course.id})
    response = api_client.patch(url, data=data)
    assert response.status_code == status.HTTP_200_OK
    response_j = response.json()
    assert response_j['id'] == course.id
    assert response_j['name'] == 'update_test'


@pytest.mark.django_db
def test_course_delete(api_client, course_factory):
    """тест успешного удаления курса"""
    course_factory(_quantity=3, name='delete_test')
    course = Course.objects.filter(name='delete_test').first()
    url = reverse('courses-detail', kwargs={'pk': course.id})
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    url = reverse('courses-list')
    response = api_client.get(url)
    assert len(response.data) == 2
