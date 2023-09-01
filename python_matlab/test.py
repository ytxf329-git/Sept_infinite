import matlab.engine
eng = matlab.engine.start_matlab()
ass = eng.ConnectPython(2,6)
print(ass)
eng.quit()