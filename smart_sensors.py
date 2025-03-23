def analyze_power_consumption(readings):
    if any(x < 10 or x > 200 for x in readings):  
        print("INVALID INPUT")
        return

    sensors = [readings[i::5] for i in range(5)]
    avg_consumptions = [round(sum(sensor) / 4) for sensor in sensors]

    max_avg = max(avg_consumptions)

    if max_avg < 50:
        print("Energy consumption is optimal.")
    else:
        print(f"Sensor Number : {avg_consumptions.index(max_avg) + 1}")

readings = list(map(int, input().split()))
analyze_power_consumption(readings)
