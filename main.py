from deep_text_recognition_benchmark.dtrb import DTRB

plate_rcognizer = DTRB("weiths/best_accuracy_license_plate_recognition_model.pth")
plate_rcognizer.predict("io/input")  


