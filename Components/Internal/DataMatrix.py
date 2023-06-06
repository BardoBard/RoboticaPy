import cv2
import pylibdmtx.pylibdmtx as dmtx
import easygui

def scan_data_matrix(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    codes = dmtx.decode(gray, timeout=500)  # Set a timeout value (in milliseconds) for code detection
    
    if len(codes) > 0:
        for code in codes:
            data = code.data.decode('utf-8')
            print("Data Matrix Code:", data)
            easygui.textbox("Scanned Data Matrix Code", "Scanned Code", data)