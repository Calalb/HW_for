class Cabinet():
    top = None
    middle = None
    bottom = None

    def putOn(self, name, thing):
        if name == 'top' and self.top == None:
            self.top = thing
        elif name == 'middle' and self.middle == None:
            self.middle = thing
        elif name == 'bottom' and self.bottom == None:
            self.bottom = thing
        else:
            print(f"Cannot place ''{thing}'' on {name} shelf, it is not empty!")

    def takeFrom(self, name):
        if name == 'top'  and self.top != None:
            self.top = None
        elif name == 'middle' and self.middle != None:
            self.middle = None
        elif name == 'bottom' and self.bottom != None:
            self.bottom = None
        else:
            print(f"Nothing to take! The {name} shelf is empty")

    def VerifTex(self):
        if self.bottom == None:
            self.bottom = ''
        if self.middle == None:
            self.middle = ''
        if self.top == None:
            self.top = ''

    def printSchema(self):
        self.VerifTex()
        line = '#'*30
        first_top = self.top
        sec_top = first_top.center(28)
        first_middle = self.middle
        sec_middle = first_middle.center(28)
        first_bottom = self.bottom
        sec_bottom = first_bottom.center(28)
        print(f" {line} \n #{sec_top}# \n {line} \n #{sec_middle}# \n {line} \n #{sec_bottom}# \n {line}")

s1 = Cabinet()
s2 = Cabinet()
s1.putOn('top', 'Mercerds')
s1.putOn('middle', 'Mazda')
s1.putOn('top', 'Opel')
s1.takeFrom('bottom')
s1.printSchema()

