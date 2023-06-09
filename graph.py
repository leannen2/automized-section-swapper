class Student:
    def __init__(self, name, offer, target):
        self.name = name
        self.offer = offer
        self.target = target

class Graph:
    def __init__(self):
        self.adjacencyDict = {}
        self.nameToStudent = {}
        self.students = {}

    def add_student(self, name, offer, target):
        if name in self.nameToStudent:
            print("student already exists")
        new_student = Student(name, offer, target)
        self.nameToStudent[name] = Student(name, offer, target)
        self.adjacencyDict[name] = []
        self.students.add(name)
        for student in self.adjacencyDict:
            if offer == self.nameToStudent[student].target:
                self.adjacencyDict[name].append(student)
            if self.nameToStudent[student].offer == target:
                self.adjacencyDict[student].append(name)

    def remove_student(self):
        pass

    def get_adjacency(self, student):
        return self.adjacencyDict[student]
    
    def get_adjacency_dict(self):
        return self.adjacencyDict

    def get_edges(self):
        edges = []
        for student in self.adjacencyDict:
            for adjacenctStudent in self.adjacencyDict[student]:
                edges.append((student, adjacenctStudent))
        return edges
    
    def get_students(self):
        return self.students
            

    

if __name__ == "__main__":
    g = Graph()
    g.add_student(1, "a", "b")
    g.add_student(2, "b", "c")
    g.add_student(3, "c", "a")
    print(g.get_edges())
    print(g.get_adjacency_dict())
