logData = sc.textFile(logFile).cache()
errors = logData.filter(lambda line: "ERROR" in line)
