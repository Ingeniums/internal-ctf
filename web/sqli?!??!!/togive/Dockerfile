# sudo docker build -t sqli .
# sudo docker run -d -p 3000:3000 --rm sqli
FROM node:16

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY ./models ./models/
COPY ./views ./views/
COPY index.js .


EXPOSE 3000

CMD ["node", "index.js"]
