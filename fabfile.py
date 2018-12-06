from fabric.api import env, local, cd, run

env.hosts = ['production']


def deploy():
    local('git push')
    with cd('~/acme_wf'):
        run('git pull')
        run('pipenv install')
