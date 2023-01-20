class printErrorFormat(object):
    @staticmethod
    def printError(theClass,theMethod,theexection):
        print("Il y a un problème au niveau de la class ",str(theClass)," sur la méthode (",str(theMethod),") qui dit ##",str(theexection.__cause__))