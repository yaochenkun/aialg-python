service nlp_alg_service {
  string hello(1: string key)
  string predict(1: double origin)
  string word_seg(1: string text)
  string word_pos(1: string text)
  string bye()
}

service image_alg_service {
  string hello(1: string key)
  string bye()
}

service speech_alg_service {
  string hello(1: string key)
  string bye()
}

service video_alg_service {
  string hello(1: string key)
  string bye()
}
