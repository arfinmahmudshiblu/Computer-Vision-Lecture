from yoloapp.utils.main_utils import encodeImagetoBase64, decodeImage


encode_img = encodeImagetoBase64("data/InputImage.jpg")

print(encode_img)

decodeImage(encode_img, "OutputImage.jpg")