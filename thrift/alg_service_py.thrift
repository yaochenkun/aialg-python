service nlp_alg_service {
  string predict(1: double origin)
  string word_seg(1: string text)
  string word_pos(1: string text)
  string word_ner(1: string text)
}

service image_alg_service {
  string face_sim(1: string img_base64_1, 2: string img_base64_2)
}

service speech_alg_service {
}

service video_alg_service {
}
