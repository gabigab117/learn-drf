# Repo to learn DRF with OpenClassroom

https://github.com/OpenClassrooms-Student-Center/7192416_APIs_DRF

# Notes

https://openclassrooms.com/fr/courses/7192416-mettez-en-place-une-api-avec-django-rest-framework/7424627-ajoutez-de-l-interaction-avec-les-actions

Vous devez penser Action chaque fois qu’un besoin fait référence à une entité, mais que le verbe ne correspond pas à un
élément du CRUD. Par exemple, dans « Nous souhaitons que nos visiteurs puissent liker des publications », l’entité est
la publication et l’action est liker.

https://openclassrooms.com/fr/courses/7192416-mettez-en-place-une-api-avec-django-rest-framework/7424627-ajoutez-de-l-interaction-avec-les-actions#/id/r-7423349

Une action se crée dans DRF en mettant en place le décorateur action  sur une méthode d’un Viewset. Les paramètres suivants sont disponibles :

methods  est la liste des méthodes HTTP qui appellent cette action, parmi GET, POST, PATCH, PUT, DELETE.

detail  est un booléen qui précise si l’action est disponible sur l’URL de liste ou de détail.

url_path  permet de déterminer l’URL qui sera ajoutée à la fin de l'endpoint de liste ou de détail. S'il n’est pas précisé, alors le nom de la méthode est utilisé.