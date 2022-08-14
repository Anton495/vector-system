import itertools as it

class FractalCurve:
    
    def __init__(self,chain_proto,base_maps,
                 dim=None,alph=None,genus=None,fractal=None,vect_dict=None):
        
        self.chain_proto = chain_proto
        self.base_maps = base_maps
        self.dim = self.get_dim()
        self.alph = self.get_alphabet()
        self.genus = self.get_genus()
        self.fractal = self.get_fractal()
        self.vect_dict = self.get_vect_dict()

    def get_dim(self):
        '''get the curve dimension'''
        return len(set(''.join(self.chain_proto[0]).lower()))

    def get_alphabet(self):
        '''get alphabet for curve prototypes and base maps'''
        return 'ijklmnop'[:self.dim]

    def get_genus(self):
        '''get the curve genus'''
        return len(self.base_maps[0])

    def get_fractal(self):
        '''get the curve fractality'''
        fractal = len(self.chain_proto)
        # Adding curve number to basic transforms for monofractals
        if fractal == 1:
            self.base_maps = [['0' + k for k in self.base_maps[0]]]  
        return fractal

    def get_vect_dict(self):
        '''get unit and diagonal vectors dictonary'''
        # Forming a dictionary of unit vectors
        vect_dict = {}
        for k in range(self.dim):
            coord = [0] * self.dim
            coord[k] = 1
            vect_dict[self.alph[k]] = coord
            vect_dict[self.alph[k].upper()] = [-m for m in coord]
        
        # This function obtains a diagonal vector from several unit vectors
        # by summing their coordinates. For example ij = i + j = [1,0] + [0,1] = [1,1]
        def get_diag_coord(vector):
            arg = [vect_dict[k] for k in vector]
            coord = list(map(sum,zip(*arg)))
            return coord
        
        # Adding diagonal steps to the dictionary
        all_letters = [[self.alph[k],self.alph[k].upper()] for k in range(self.dim)]
        for m in range(2,self.dim+1):
            all_comb_let = list(it.permutations(all_letters,m))
            all_diag_coord = list(map(''.join, it.chain(*[it.product(*k) for k in all_comb_let])))
            for k in all_diag_coord:
                vect_dict[k] = get_diag_coord(k)
        
        return vect_dict
    
    def get_fraction(self,sub,bm):
        '''apply base map and reverse to some curve fraction'''
        # Checking for the presence of a time reversal in the base transformation
        if bm[-1] == '~':
            # Changing vector directions
            bm = bm[:-1].swapcase()
            # Проходим вектора в обратном порядке
            sub = reversed(sub)
            
        # Creating a base transformation dictionary, e.g. kIJ = {k->i,I->j,J->k} 
        # and its inversion {K->I,i->j,j->K}
        dict_bm={}
        for k in range(self.dim):
            dict_bm[bm[k]] = self.alph[k]
            dict_bm[bm[k].swapcase()] = self.alph[k].upper()
            
        # Rotating the fraction (using a dictionary)
        fraction = [''.join(list(map(dict_bm.get, k))) for k in sub]
        
        return fraction
    
    def get_subdiv(self,sub_numb):
        '''get n-th curve subdivision'''
        # Determining the zero division of the curve
        sub_k = self.chain_proto
        
        for n in range(sub_numb):

            # Forming a list of transformed factions
            sub_n = [[self.get_fraction(sub_k[int(self.base_maps[k][m][0])],self.base_maps[k][m][1:]) 
                      for m in range(self.genus)] for k in range(self.fractal)]
            
            # Adding connecting edges between fractions for the figure
            [[sub_n[k].insert(2*m+1,[self.chain_proto[k][m]])
              for m in range(self.genus-1)] for k in range(self.fractal)]
            
            # Consolidation of all factions into one faction
            sub_n = [sum(k,[]) for k in sub_n]
            
            # Defining the (n-1)-th division as the n-th division
            sub_k = sub_n.copy()
        
        return sub_k
    
    def get_curve_coord(self,chain_code,start=None):
        '''chain code => vectors => coordinates'''
        # Passing from chain code to unit vectors (using a dictionary) 
        subdiv = list(map(self.vect_dict.get,chain_code))
                    
        # Determining the start coordinate for a curve
        curve_coord = [[0]*self.dim] + subdiv if start == None else [start] + subdiv
        
        # Passing from unit vectors to curve coordinates (summing coordinates)
        curve_coord = list(zip(*map(it.accumulate, zip(*curve_coord))))
        
        return curve_coord    
