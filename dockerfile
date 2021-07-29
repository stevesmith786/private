# Install requirements
RUN pip3 install -U -r requirements.txt
CMD ["bash","startup.sh"]