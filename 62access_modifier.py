class Employee:
    def __init__(self):
        self._name = "Arya"

a = Employee()
# print(a.__name) cannot be accesed directly
print(a._name) # can be accesed indirectly
# print(a.__dir__())


#  private _classname_ _attributename
#  protected _attribute
#  public 