from pprintpp import pprint as pp
from db.database import Graph
from helper.write_a_json import write_a_json as wj


class Grafico():
    def __init__(self):
        self.db = Graph(uri='bolt://18.234.187.109:7687', user='neo4j', password='loops-swamp-chits')

    def read_by_professor(self, teacher):
        return self.db.execute_query('MATCH (t:Teacher {name:$name}) RETURN (t.ano_nasc), (t.cpf)',
                                     {'name': teacher['name']})

    def read_all_nodes(self):
        return self.db.execute_query('MATCH (n) RETURN n')

    def read_by_letter(self, letter):
        return self.db.execute_query('MATCH (n:Teacher) WHERE n.name STARTS WITH $letter RETURN (n.name), (n.cpf)',
                                     {'letter': letter})
    def read_by_city(self):
        return self.db.execute_query('MATCH (n:City) RETURN (n.name)')
    def read_by_school(self):
        #MATCH (n:School) MATCH (n:School) WHERE n.number >=150 and  n.number <=550 return n; return n;
        return self.db.execute_query('MATCH (n:School ) WHERE (n.number >=150) and  (n.number <=550) RETURN (n.name)')
    def read_by_ano_nasc(self):
        return self.db.execute_query('MATCH (n:Teacher) RETURN MIN(n.ano_nasc), MAX(n.ano_nasc)')
    def read_by_media(self):
        return self.db.execute_query('MATCH (n:City) RETURN AVG(n.population)')
    def read_by_cep(self, cep):
        return self.db.execute_query('MATCH (n:City) WHERE n.cep = $cep RETURN REPLACE(n.name, "a", "A")',
                                     {'cep': cep})
    def read_by_professor_nome(self):
        return self.db.execute_query('MATCH(t:Teacher)  RETURN substring(t.name, 1, 3);')

class TeacherCRUD(Grafico):
    def __init__(self):
        super().__init__()

    def create_professor(self, name, ano_nasc, cpf):
        return self.db.execute_query('CREATE (n:Teacher {name:$name, ano_nasc:$ano_nasc, cpf:$cpf}) return n',
                                     {'name': name, 'ano_nasc': ano_nasc, 'cpf': cpf})
    def read_by_name(self, name):
        return self.db.execute_query('MATCH (n:Teacher {name:$name}) RETURN n',
                                     {'name': name})
    def update(self, name, newCpf):
        return self.db.execute_query('MATCH (n:Teacher {name:$name}) SET n.cpf = $newCpf RETURN n',
                                     {'name': name, 'newCpf': newCpf})
    def delete(self, name):
        return self.db.execute_query('MATCH (n:Teacher {name:$name}) DETACH DELETE n',
                                     {'name': name})
db = Grafico()
db1 = TeacherCRUD()
# Questão 01
# A - MATCH(t:Teacher) WHERE t.name = 'Renzo' return (t.ano_nasc), (t.cpf);
"""teacher = {'name': 'Renzo'}
aux = db.read_by_professor(teacher)
aux1 = db.read_all_nodes()
pp(aux)
wj(aux, '1A')"""

# B - MATCH(t:Teacher) WHERE t.name STARTS WITH  'M' return (t.ano_nasc), (t.cpf);
"""letter = 'M'
aux = db.read_by_letter(letter)
pp(aux)
wj(aux, '1B')"""

# C - MATCH (n:City) RETURN n.name;
"""aux = db.read_by_city()
pp(aux)
wj(aux, '1C')"""

# D - MATCH (n:School) WHERE n.number >=150 and  n.number <=550 return n;
"""aux = db.read_by_school()
pp(aux)
wj(aux, '1D')
print('Fim')"""

# Questão 02
# A - MATCH(t:Teacher) RETURN MIN(t.ano_nasc), MAX(t.ano_nasc);
"""aux = db.read_by_ano_nasc()
pp(aux)
wj(aux, '2A')"""

# B - MATCH(c:City) RETURN AVG(c.population);
"""aux = db.read_by_media()
pp(aux)
wj(aux, '2B')"""

# C - MATCH(c:City) WHERE (c.cep = '37540-000') return REPLACE(c.name,"a","A");
"""cep = '37540-000'
aux = db.read_by_cep(cep)
pp(aux)
wj(aux, '2C')"""

# D - MATCH(t:Teacher)  RETURN substring(t.name, 1, 3);
"""aux = db.read_by_professor_nome()
pp(aux)
wj(aux, '2D')"""

# Questão 03
# A
"""print('Entre com os dados do professor')
name = input('  Name: ')
ano_nasc = input('   Ano de nascimento : ')
cpf = input('  Cpf : ')
aux = db1.create_professor(name, ano_nasc, cpf)
pp(aux)
wj(aux, '3A')"""

# B
"""name = input('Entre com o nome do professor: ')
aux = db1.read_by_name(name)
pp(aux)
wj(aux, '3B')"""

# C
"""name = input('Entre com o nome do professor: ')
newCpf = input('Entre com o novo cpf: ')
aux = db1.update(name, newCpf)
pp(aux)
wj(aux, '3C')"""

# D
name = input('Entre com o nome do professor que deseja deletar: ')
aux = db1.delete(name)
pp(aux)
wj(aux, '3D')
