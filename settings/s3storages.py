from storages.backends.s3boto import S3BotoStorage
StaticStorage = lambda: S3BotoStorage(bucket='STATIC_BUCKET_NAME')
MediaStorage  = lambda: S3BotoStorage(bucket='MEDIA_BUCKET_NAME')