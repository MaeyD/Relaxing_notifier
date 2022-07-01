import time
from plyer import notification
if __name__ == '__main__':
 	while True:
 		notification.notify(
 			title = "!! RELAX !!",
 			message ="~ Take a break ~ Straighten your posture ~ Relax your eyes ~ Look away from screen ~ Drink some water ~",
 			timeout= 15
 			)
 		time.sleep(60*30)
