# Stage 1: Build the Vue.js app
FROM node:22-alpine AS build-stage

WORKDIR /app

# Install dependencies
COPY package*.json .
RUN npm install

COPY . .
RUN npm run build



FROM nginx:alpine


COPY --from=build-stage /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
