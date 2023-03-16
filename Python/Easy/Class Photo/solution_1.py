#Sorting Algorithms takes nlog(n) time complexity. We dont store anything so its (1)
#Sum up, Time Complexity O(nlog(n)) | Space O(1)

def classPhotos(redShirtHeights, blueShirtHeights) -> bool:

    redShirtHeights.sort()
    blueShirtHeights.sort()

    shortColorFirstLine = "RED" if redShirtHeights[0] > blueShirtHeights[0] else "BLUE"
    
    if shortColorFirstLine == "BLUE":

        for idx , heightInBlue in enumerate(blueShirtHeights):
            heightInRed = redShirtHeights[idx]

            if heightInBlue <= heightInRed:
                return False

    if shortColorFirstLine == "RED":

        for idx , heightInRed in enumerate(redShirtHeights):
            heightInBlue = blueShirtHeights[idx]

            if heightInRed <= heightInBlue:
                return False
        
    return True
