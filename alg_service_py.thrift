service nlp_alg_service {
  string predict(1: double origin)
  string word_seg(1: string text)
  string word_pos(1: string text)
}

service image_alg_service {
}

service speech_alg_service {
}

service video_alg_service {
}
