# build stage
FROM node:15.13-alpine as build-stage
WORKDIR /app/
COPY frontend/vue/package.json /app/
RUN npm cache verify
RUN npm install
COPY frontend/vue/ /app/
RUN npm run build

# production stage
FROM nginx:latest as production-stage
COPY nginx/nginx-conf.conf /etc/nginx/nginx.conf
COPY backend/static /usr/src/app/static/
COPY --from=build-stage /app/dist /dist/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]