service NlpAlgService {
  string predict(1: double origin)
  string word_seg(1: string text)
  string word_pos(1: string text)
}

service ImageAlgService {
}

service SpeechAlgService {
}

service VideoAlgService {
}
