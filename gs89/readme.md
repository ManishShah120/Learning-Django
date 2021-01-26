# Signals and Built-in Signals

## log-In & Log-Out Signals
- `user_logged_in`
- `user_logged_out`
- `user_login_failed`

## Model signals
- `pre_init(sender, args, kwargs)`
- `post_init(sender, instance)`
- `pre_save(sender, instance, raw, using, update_fields)`
- `post_save(sender, instance, created, raw, using, update_fields)`
- `pre_delete(sender, instance, using)`
- `post_delete(sender, instance, using)`
- `m2m_changed(sender, instance, action, reverse, model, pk_set, using)`
- `class_prepared(sender)`

## Request/Response Signals
- `request_started(sender, environ)`
- `request_finished(sender)`
- `got_request_exception(sender, request)`

## Management signals
- `pre_migrate(sender, app_config, verbosity, interactive, using, plan, apps)`
- `post_migrate(sender, app_config, verbosity, interactive, using, plan, apps)`

## Test Signals
- `setting_changed(sender, setting, value, enter)`

## Database Wrappers
- `connection_created`