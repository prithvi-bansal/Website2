from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver, Signal
from django.db.models.signals import ( pre_save, pre_delete, pre_init, post_save, post_delete,
post_init, pre_migrate, post_migrate, m2m_changed )
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created
from posts.models import Post

# # Custom Signal
# notification = Signal()

# @receiver(notification)
# def show_notification(sender, **kwargs):
# 	print('--------------------------')
# 	print(sender)
# 	print(f'{kwargs}')
# 	print("notification")
# 	print('--------------------------')


# # @receiver(m2m_changed, sender=Post.likes.through)
# def post_likes_signal(sender, **kwargs):
# 	print('------------')
# 	print(sender)        
# 	print(f'{kwargs}')	 	
# 	print('------------')
# m2m_changed.connect(post_likes_signal, sender=Post.likes.through)


# @receiver(user_logged_in, sender=User)
# def login_success(sender, request, user, **kwargs):
# 	print('--------------------------')
# 	print("Logged in Successfully")
# 	print("Sender:",sender)
# 	print("request:",request)
# 	print("user:",user)
# 	print("password:",user.password)
# 	print(f'kwargs:{kwargs}')
# 	print('--------------------------')
# # user_logged_in.connect(login_success, sender=User)

# @receiver(user_logged_out, sender=User)
# def logout_success(sender, request, user, **kwargs):
# 	print('--------------------------')
# 	print("Logged out Successfully")
# 	print("Sender:",sender)
# 	print("request:",request)
# 	print("user:",user.password)
# 	print(f'kwargs:{kwargs}')
# 	print('--------------------------')
# # user_logged_out.connect(logout_success, sender=User)

# @receiver(user_login_failed)
# def Login_failed(sender, request, credentials, **kwargs):
# 	print('--------------------------')
# 	print("Username or Password are incorrect")
# 	print("Sender:",sender)
# 	print("request:",request)
# 	print("credentials:",credentials)
# 	print(f'kwargs:{kwargs}')
# 	print('--------------------------')
# # user_login_failed.connect(Login_failed)

# @receiver(pre_save, sender=User)
# def pre_save_signal(sender, instance, **kwargs):
# 	print('--------------------------')
# 	print("Pre Save Signal")
# 	print("Sender:",sender)
# 	print("instance:", instance)
# 	print(f'kwargs:{kwargs}')
# 	print('--------------------------')
# # pre_save.connect(pre_save_signal, sender=User)

# @receiver(post_save, sender=User)
# def post_save_signal(sender, instance, created, **kwargs):
# 	print('--------------------------')
# 	if created:
# 		print("Post Save Signal")
# 		print("New Record")
# 		print("Sender:",sender)
# 		print("instance:", instance)
# 		print("created:", created)
# 		print(f'kwargs:{kwargs}')
# 	else:
# 		print("Post Save Signal")
# 		print("Update")
# 		print("Sender:",sender)
# 		print("instance:", instance)
# 		print("created:", created)
# 		print(f'kwargs:{kwargs}')
# 	print('--------------------------')
# # post_save.connect(post_save_signal, sender=User)

# @receiver(pre_delete, sender=User)
# def pre_delete_signal(sender, instance, **kwargs):
# 	print('--------------------------')
# 	print("Pre Delete Signal")
# 	print("Sender:",sender)
# 	print("instance:", instance)
# 	print(f'kwargs:{kwargs}')
# 	print('--------------------------')
# # pre_delete.connect(pre_delete_signal, sender=User)

# @receiver(post_delete, sender=User)
# def post_delete_signal(sender, instance, **kwargs):
# 	print('--------------------------')
# 	print("Post Delete Signal")
# 	print("Sender:",sender)
# 	print("instance:", instance)
# 	print(f'kwargs:{kwargs}')
# 	print('--------------------------')
# # post_delete.connect(post_delete_signal, sender=User)

# @receiver(pre_init, sender=User)
# def pre_init_signal(sender, *args, **kwargs):
# 	print('--------------------------')
# 	print("Pre Init Signal")
# 	print("Sender:",sender)
# 	print(f'args:{args}')
# 	print(f'kwargs:{kwargs}')
# 	print('--------------------------')
# # pre_init.connect(pre_init_signal, sender=User)

# @receiver(post_init, sender=User)
# def post_init_signal(sender, *args, **kwargs):
# 	print('--------------------------')
# 	print("Post Init Signal")
# 	print("Sender:",sender)
# 	print(f'args:{args}')
# 	print(f'kwargs:{kwargs}')
# 	print('--------------------------')
# # post_init.connect(post_init_signal, sender=User)

# @receiver(request_started)
# def request_started_signal(sender, environ, **kwargs):
# 	print('--------------------')
# 	print("Request Started Signal")
# 	print("sender:", sender)
# 	print("environ:", environ)
# 	print(f'kwargs:{kwargs}')
# 	print('--------------------')
# # request_started.connect(request_started_signal)

# @receiver(request_finished)
# def request_finished_signal(sender, **kwargs):
# 	print('--------------------')
# 	print("Request Finished Signal")
# 	print("sender:", sender)
# 	print(f'kwargs:{kwargs}')
# 	print('--------------------')
# # request_finished.connect(request_finished_signal)

# @receiver(got_request_exception)
# def request_exception_signal(sender, request, **kwargs):
# 	print('--------------------')
# 	print("Request Exception Signal")
# 	print("sender:", sender)
# 	print("Request:", request)
# 	print(f'kwargs:{kwargs}')
# 	print('--------------------')
# # got_request_exception.connect(request_finished_signal)

# @receiver(pre_migrate)
# def pre_migrate_signal(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
# 	print('---------------------------')
# 	print("Before Migrate Signal")
# 	print('sender:', sender)
# 	print('app_config:', app_config)
# 	print('verbosity:', verbosity)
# 	print('interactive:', interactive)
# 	print('using:', using)
# 	print('plan:', plan)
# 	print('apps:', apps)
# 	print(f'kwargs:{kwargs}')
# 	print('---------------------------')
# # pre_migrate.connect(pre_migrate_signal)

# @receiver(post_migrate)
# def post_migrate_signal(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
# 	print('---------------------------')
# 	print("After Migrate Signal")
# 	print('sender:', sender)
# 	print('app_config:', app_config)
# 	print('verbosity:', verbosity)
# 	print('interactive:', interactive)
# 	print('using:', using)
# 	print('plan:', plan)
# 	print('apps:', apps)
# 	print(f'kwargs:{kwargs}')
# 	print('---------------------------')
# # post_migrate.connect(post_migrate_signal)

# @receiver(connection_created)
# def connection_db(sender, connection, **kwargs):
# 	print('------------------------')
# 	print("Connection to the Database")
# 	print("Sender:", sender)
# 	print("connection:", connection)
# 	print(f'kwargs:{kwargs}')
# 	print('------------------------')
# # connection_created.connect(connection_db)

