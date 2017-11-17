service NlpAlgThriftService {
  string predict(1: double origin)
  string wordSeg(1: string text)
  string wordPos(1: string text)
}

service ImageAlgThriftService {
}

service SpeechAlgThriftService {
}

service VideoAlgThriftService {
}
