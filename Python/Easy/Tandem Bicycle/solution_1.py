def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):

    sumOfSpeeds = 0
    redShirtSpeeds.sort()
    

    if fastest == True:
        blueShirtSpeeds.sort()

        for i in range(len(redShirtSpeeds)):
            redShirtSpeed = redShirtSpeeds[len(redShirtSpeeds) - (i + 1)]
            blueShirtSpeed = blueShirtSpeeds[i]

            pairedMaxSpeed = max(redShirtSpeed , blueShirtSpeed)

            sumOfSpeeds += pairedMaxSpeed

    if fastest == False:
        blueShirtSpeeds.sort(reverse=True)

        for i in range(len(redShirtSpeeds)):
            redShirtSpeed = redShirtSpeeds[len(redShirtSpeeds) - (i + 1)]
            blueShirtSpeed = blueShirtSpeeds[i]

            pairedMaxSpeed = max(redShirtSpeed , blueShirtSpeed)

            sumOfSpeeds += pairedMaxSpeed


    return sumOfSpeeds
