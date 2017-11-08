service NlpAlgService {
  string hello(1: string key)
  string predict(1: double origin)
  string bye()
}

service ImageAlgService {
  string hello(1: string key)
  string bye()
}

service SpeechAlgService {
  string hello(1: string key)
  string bye()
}

service VideoAlgService {
  string hello(1: string key)
  string bye()
}
