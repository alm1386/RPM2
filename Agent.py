#Amber Montgomery
#references used: Exemplary Work posted in Resources
# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
from PIL import Image, ImageFilter, ImageOps, ImageChops, ImageStat
import math, copy

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an integer representing its
    # answer to the question: "1", "2", "3", "4", "5", or "6". These integers
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName() (as Strings).
    #
    # In addition to returning your answer at the end of the method, your Agent
    # may also call problem.checkAnswer(int givenAnswer). The parameter
    # passed to checkAnswer should be your Agent's current guess for the
    # problem; checkAnswer will return the correct answer to the problem. This
    # allows your Agent to check its answer. Note, however, that after your
    # agent has called checkAnswer, it will *not* be able to change its answer.
    # checkAnswer is used to allow your Agent to learn from its incorrect
    # answers; however, your Agent cannot change the answer to a question it
    # has already answered.
    #
    # If your Agent calls checkAnswer during execution of Solve, the answer it
    # returns will be ignored; otherwise, the answer returned at the end of
    # Solve will be taken as your Agent's answer to this problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.

    #convert image to negative for processing
    def convertImage(self,image):
        image = image.convert(mode="L")
        image_negative = ImageOps.invert(image)
        return image_negative

    #determine if images are the same
    def same(image1, image2):
        neg_image1 = convertImage(image1)
        neg_image2 = convertImage(image2)

        diff = ImageChops.difference(neg_image1, neg_image2)

        stat = ImageStat.Stat(diff)
        mean = stat.mean[0]
        #print (mean)

        if mean < 1.0:
            print ("Same function: These 2 images are the SAME")
            return True
        else:
            print ("Same function: These 2 images are not the same.")
            return False

    #determine the angle of rotation it takes to change image 1 into image 2
    def rotate(image1, image2):
        neg_image1 = convertImage(image1)
        neg_image2 = convertImage(image2)
        angle = 0

        #Visual testing of presumed answer
        #answer = neg_image1.rotate(90)
        #answer.show()
        #neg_image2.show()

        for angle in range(0,360):
            rotated_image1 = neg_image1.rotate(angle)

            diff = ImageChops.difference(rotated_image1, neg_image2)

            stat = ImageStat.Stat(diff)
            mean = stat.mean[0]

            if mean < 1.0:
                print ("Rotate function: The angle is ", angle)
                return angle

        print ("Rotate function: Image 1 cannot be rotated to match Image 2")
        return False

    #determine if vertical reflection turns image 1 into image 2
    def verticalReflection(image1, image2):
        neg_image1 = convertImage(image1)
        neg_image2 = convertImage(image2)

        reflected_image1 = ImageOps.flip(neg_image1)

        diff = ImageChops.difference(reflected_image1, neg_image2)
        stat = ImageStat.Stat(diff)
        mean = stat.mean[0]

        if mean < 1.0:
            print ("Vertical Reflection Function: Reflected Vertically")
            return True
        else:
            print ("Vertical Reflection Function: Not reflected vertically")
            return False

    #determine if horizontal reflection (mirroring) turns image 1 into image 2
    def horizontalReflection(image1, image2):
        neg_image1 = convertImage(image1)
        neg_image2 = convertImage(image2)

        reflected_image1 = ImageOps.mirror(neg_image1)

        diff = ImageChops.difference(reflected_image1, neg_image2)
        stat = ImageStat.Stat(diff)
        mean = stat.mean[0]

        if mean < 1.0:
            print ("Horizontal Reflection Function: Reflected Horizontally")
            return True
        else:
            print ("Horizontal Reflection Function: Not reflected horizontally")
            return False



    def Solve(self,problem):


        for figureID in problem.figures.keys():
            problemFigure = problem.figures[figureID]
            print ("Figure: ", problemFigure.visualFilename)
            filename = problemFigure.visualFilename
            convertImage(filename[0])
            same(filename[0], filename[1])

            """
            for objectID in problemFigure.objects.keys():
                figObject = problemFigure.objects[objectID]
                print ("Figure Object: ", figObject.name)

                for attributeID in figObject.attributes.keys():
                    figAttributes = figObject.attributes[attributeID]
                    print (attributeID,": ", figAttributes)
            """


        return -1
