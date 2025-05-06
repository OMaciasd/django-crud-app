DB_USER=myuser
DB_PASSWORD=mypassword
SECRET_KEY=mysecretkey

gcloud secrets create db-user --replication-policy="automatic"
gcloud secrets create db-password --replication-policy="automatic"
gcloud secrets create secret-key --replication-policy="automatic"

echo -n "myuser" | gcloud secrets versions add db-user --data-file=-
echo -n "mypassword" | gcloud secrets versions add db-password --data-file=-
echo -n "mysecretkey" | gcloud secrets versions add secret-key --data-file=-

gcloud projects add-iam-policy-binding TU_PROYECTO_ID \
  --member=serviceAccount:$(gcloud projects describe TU_PROYECTO_ID --format='value(projectNumber)')@cloudbuild.gserviceaccount.com \
  --role=roles/secretmanager.secretAccessor
