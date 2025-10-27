# docker stop python-test # no need since it doesn't constantly run
# docker rm python-test
# docker rmi python

docker stop mysql-db
docker rm mysql-db
# docker rmi mysql # no need to delete the image since we get it from registry