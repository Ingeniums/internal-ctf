# sudo docker build -t nosqli .
# sudo docker run -d -p 3000:3000 --rm nosqli
FROM node:16

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY ./models ./models/
COPY ./views ./views/
COPY index.js .


EXPOSE 3000

CMD ["node", "index.js"]
