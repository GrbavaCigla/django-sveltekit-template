# Django &amp; Sveltekit template
Template for Django/Sveltekit stack

## Table of contents
1. [Configuration](#configuration)
2. [License](#license)

## Configuration

| Variable                   | Default                              | Note                         |
|----------------------------|--------------------------------------|------------------------------|
| `DJANGO_SECRET_KEY`        | get_random_secret_key()              |                              |
| `DJANGO_DEBUG`             | True                                 |                              |
| `FRONTEND_HOST`            | `http://localhost:5173`              |                              |
| `DJANGO_CORS_ORIGINS`      | [`FRONTEND_HOST`]                    | Hosts are separated by comma |
| `DJANGO_ALLOWED_HOSTS`     | []                                   | Hosts are separated by comma |
| `DJANGO_ACTIVATION_URL`    | 'api/v1/auth/activate/{uid}/{token}' | Used for register activation |
|                            |                                      |                              |
| `DJANGO_DB`                | sqlite                               | `postgresql` or `sqlite`     |
| `DJANGO_POSTGRES_HOST`     | 'localhost'                          |                              |
| `DJANGO_POSTGRES_NAME`     | 'postgres'                           |                              |
| `DJANGO_POSTGRES_USER`     | 'postgres'                           |                              |
| `DJANGO_POSTGRES_PASSWORD` | 'postgres'                           |                              |
| `DJANGO_POSTGRES_PORT`     | 5432                                 |                              |
|                            |                                      |                              |
| `DJANGO_EMAIL_HOST`        | ''                                   |                              |
| `DJANGO_EMAIL_PORT`        | 587                                  |                              |
| `DJANGO_EMAIL_USER`        | ''                                   |                              |
| `DJANGO_EMAIL_PASSWORD`    | ''                                   |                              |




## License
Project is licensed under [GPLv3](https://github.com/GrbavaCigla/razmenakarata/blob/master/LICENSE) license.
