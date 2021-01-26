from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):

    print("----------------------------")
    print("Logged-in Signal... Run Into..")
    print("Sender:", sender)
    print("Request:", request)
    print("User:", user)
    print(f'Kwargs: {kwargs}')

    # we can also using this instead of decorator
    # user_logged_in.connect(login_success, sender=User)


@receiver(user_logged_out, sender=User)
def log_out(sender, request, user, **kwargs):

    print("----------------------------")
    print("Logged-Out Signal... Run Outro..")
    print("Sender: ", sender)
    print("Request: ", request)
    print("User: ", user)
    print(f'Kwargs: {kwargs}')

    # user_logged_out.connect(log_out, sender=User)


@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):

    print("----------------------------")
    print("Logged-In Failed Signal...")
    print("Sender: ", sender)
    print("Request: ", request)
    print("Credential: ", credentials)
    print(f'Kwargs: {kwargs}')

    # user_login_failed.connect(login_failed)


@receiver(pre_save, sender=User)
def at_begining_save(sender, instance, **kwargs):
    print("--------------------------")
    print("Pre Save Signal...")
    print("Sender: ", sender)
    print("Intance: ", instance)
    print(f'Kwargs: {kwargs}')


@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        print("--------------------------")
        print("Post Save Signal...")
        print("New Record")
        print("Sender: ", sender)
        print("Intance: ", instance)
        print("Created: ", created)
        print(f'Kwargs: {kwargs}')
    else:
        print("--------------------------")
        print("Post Save Signal...")
        print("Update")
        print("Sender: ", sender)
        print("Intance: ", instance)
        print("Created: ", created)
        print(f'Kwargs: {kwargs}')


@receiver(pre_delete, sender=User)
def at_begining_delete(sender, instance, **kwargs):
    print("----------------------")
    print("Pre Delete.......")
    print("Sender: ", sender)
    print("Instance: ", instance)
    print(f'Kwargs: {kwargs}')


@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    print("------------------------")
    print("At Ending Delete.........")
    print("Sender: ", sender)
    print("Instance: ", instance)
    print(f'kwargs: {kwargs}')


@receiver(pre_init, sender=User)
def at_begining_init(sender, *args, **kwargs):
    print("-------------------")
    print("Pre Init Signal.......")
    print("Sender: ", sender)
    print(f'Args: {args}')
    print(f'Kwargs: {kwargs}')


@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    print("----------------------")
    print("Post Init Signal......")
    print("Sender: ", sender)
    print(f'Args: {args}')
    print(f'Kwargs: {kwargs}')


@receiver(request_started)
def at_begining_request(sender, environ, **kwargs):
    print("--------------------")
    print("At Begining Request........")
    print("Sender: ", sender)
    print("Environ: ", environ)
    print(f'kwargs: {kwargs}')


@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print("-------------------")
    print("At Ending Request......")
    print("Sender: ", sender)
    print(f'kwargs: {kwargs}')

@receiver(got_request_exception)
def at_req_exception(sender, request, **kwargs):
    print("------------------")
    print("At Request Exception..........")
    print("Sender: ", sender)
    print("Request: ", request)
    print(f'kwargs: {kwargs}')

@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("------------------------------------")
    print("before_install_app.....")
    print("Sender: ", sender)
    print("App_config: ", app_config)
    print("Verbosity: ", verbosity)
    print("Interactive: ", interactive)
    print("Using: ", using)
    print("Plan: ", plan)
    print("App: ", apps)
    print(f'kwargs: {kwargs}')

@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("------------------------------------")
    print("at_end_migrate_flush.....")
    print("Sender: ", sender)
    print("App_config: ", app_config)
    print("Verbosity: ", verbosity)
    print("Interactive: ", interactive)
    print("Using: ", using)
    print("Plan: ", plan)
    print("App: ", apps)
    print(f'kwargs: {kwargs}')

@receiver(connection_created)
def conn_db(sender, connection, **kwargs):
    print("------------------------")
    print("Initial connection to the database")
    print("Sender: ", sender)
    print("Connection: ", connection)
    print(f'Kwargs: {kwargs}')
