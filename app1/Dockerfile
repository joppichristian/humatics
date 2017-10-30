#Dockerfile


#FROM directive instructing base image to build upon
FROM python:3-onbuild

# COPY startup script into known file location in container
COPY start.sh /start.sh

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

CMD ["cd helloworld"]
CMD ["python3 manage.py collectstatic"]
CMD ["python3 manage.py syncdb"]
CMD ["python3 manage.py makemigrations"]
CMD ["python3 manage.py migrate"]
CMD ["cd .."]
# CMD specifcies the command to execute to start the server running.
CMD ["/start.sh"]
# done!