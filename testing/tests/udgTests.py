
from PythonJoernTests import *

class UDGTests(PythonJoernTests):
    
    def testComplexArg(self):
        
        query = """getFunctionASTsByName('complexInArgs')
        .astNodes().filter{ it.type == 'Argument'}
        .uses().code
        """
        x = self.j.runGremlinQuery(query)
        self.assertEquals(len(x), 3)

    def testStatementContainingCall(self):
        
        query = """getFunctionASTsByName('complexInArgs')
        .astNodes().filter{ it.type == 'Argument'}
        .statements()
        .uses().code
        """
        x = self.j.runGremlinQuery(query)
        self.assertEquals(len(x), 4)
        

    def testComplexAssign(self):
        
        query = """getFunctionASTsByName('complexAssign')
        .astNodes().filter{ it.type == 'AssignmentExpr'}
        .defines().code
        """
        x = self.j.runGremlinQuery(query)
        self.assertEquals(x[0], 'pLtv -> u . u16')

    def testConditionalExpr(self):
        
        query = """getFunctionASTsByName('conditional_expr')
        .astNodes()
        .filter{ it.type == 'Condition'}
        .uses()
        .code
        """
        x = self.j.runGremlinQuery(query)
        self.assertEquals(len(x), 1)
