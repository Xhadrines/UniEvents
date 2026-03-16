FROM node:25.7.0

WORKDIR /frontend

COPY package.json package-lock.json ./ 
RUN npm install

COPY . .

EXPOSE 2002

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "2002"]
