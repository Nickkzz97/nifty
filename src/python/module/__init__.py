from _nifty import *









def __addStaticMethodsToUndirectedGraphAndMulticutObjectiveUndirectedGraph():

    G = graph.UndirectedGraph
    O = graph.multicut.MulticutObjectiveUndirectedGraph

    def multicutVerboseVisitor(visitNth=1):
        return graph.multicut.MulticutVerboseVisitorUndirectedGraph(visitNth)
    G.multicutVerboseVisitor = staticmethod(multicutVerboseVisitor)
    O.multicutVerboseVisitor = staticmethod(multicutVerboseVisitor)

    def greedyAdditiveProposals(sigma=1.0, weightStopCond=0.0, nodeNumStopCond=-1.0):
        s = graph.multicut.FusionMoveBasedGreedyAdditiveProposalGenSettingsUndirectedGraph()
        s.sigma = float(sigma)
        s.weightStopCond = float(weightStopCond)
        s.nodeNumStopCond = float(nodeNumStopCond)
        return s
    G.greedyAdditiveProposals = staticmethod(greedyAdditiveProposals)
    O.greedyAdditiveProposals = staticmethod(greedyAdditiveProposals)

    def watershedProposals(sigma=1.0, seedFraction=0.0):
        s = graph.multicut.FusionMoveBasedWatershedProposalGenSettingsUndirectedGraph()
        s.sigma = float(sigma)
        s.seedFraction = float(seedFraction)
        return s
    G.watershedProposals = staticmethod(watershedProposals)
    O.watershedProposals = staticmethod(watershedProposals)

    def greedyAdditiveFactory(verbose=0):
        s = graph.multicut.MulticutGreedyAdditiveSettingsUndirectedGraph()
        s.verbose = int(verbose)
        factory = graph.multicut.MulticutGreedyAdditiveFactoryUndirectedGraph(s)
        return factory
    G.greedyAdditiveFactory = staticmethod(greedyAdditiveFactory)
    O.greedyAdditiveFactory = staticmethod(greedyAdditiveFactory)


    def ilpSettings(relativeGap=0.0, absoluteGap=0.0, memLimit=-1.0):
        s = graph.multicut.IlpBackendSettings()
        s.relativeGap = float(relativeGap)
        s.absoluteGap = float(absoluteGap)
        s.memLimit = float(memLimit)

        return s
    G.ilpSettings = staticmethod(ilpSettings)
    O.ilpSettings = staticmethod(ilpSettings)

    def multicutIlpCplexFactory(verbose=0, addThreeCyclesConstraints=True,
                                addOnlyViolatedThreeCyclesConstraints=True,
                                relativeGap=0.0, absoluteGap=0.0, memLimit=-1.0):
        s = graph.multicut.MulticutIlpCplexSettingsUndirectedGraph()
        s.verbose = int(verbose)
        s.addThreeCyclesConstraints = bool(addThreeCyclesConstraints)
        s.addOnlyViolatedThreeCyclesConstraints = bool(addOnlyViolatedThreeCyclesConstraints)
        s.ilpSettings = ilpSettings(relativeGap=relativeGap, absoluteGap=absoluteGap, memLimit=memLimit)
        factory = graph.multicut.MulticutIlpCplexFactoryUndirectedGraph(s)
        return factory
    G.multicutIlpCplexFactory = staticmethod(multicutIlpCplexFactory)
    O.multicutIlpCplexFactory = staticmethod(multicutIlpCplexFactory)

    def multicutIlpGurobiFactory(verbose=0, addThreeCyclesConstraints=True,
                                addOnlyViolatedThreeCyclesConstraints=True,
                                relativeGap=0.0, absoluteGap=0.0, memLimit=-1.0):
        s = graph.multicut.MulticutIlpGurobiSettingsUndirectedGraph()
        s.verbose = int(verbose)
        s.addThreeCyclesConstraints = bool(addThreeCyclesConstraints)
        s.addOnlyViolatedThreeCyclesConstraints = bool(addOnlyViolatedThreeCyclesConstraints)
        s.ilpSettings = ilpSettings(relativeGap=relativeGap, absoluteGap=absoluteGap, memLimit=memLimit)
        factory = graph.multicut.MulticutIlpGurobiFactoryUndirectedGraph(s)
        return factory
    G.multicutIlpGurobiFactory = staticmethod(multicutIlpGurobiFactory)
    O.multicutIlpGurobiFactory = staticmethod(multicutIlpGurobiFactory)

    def multicutIlpGlpkFactory(verbose=0, addThreeCyclesConstraints=True,
                                addOnlyViolatedThreeCyclesConstraints=True,
                                relativeGap=0.0, absoluteGap=0.0, memLimit=-1.0):
        s = graph.multicut.MulticutIlpGlpkSettingsUndirectedGraph()
        s.verbose = int(verbose)
        s.addThreeCyclesConstraints = bool(addThreeCyclesConstraints)
        s.addOnlyViolatedThreeCyclesConstraints = bool(addOnlyViolatedThreeCyclesConstraints)
        s.ilpSettings = ilpSettings(relativeGap=relativeGap, absoluteGap=absoluteGap, memLimit=memLimit)
        factory = graph.multicut.MulticutIlpGlpkFactoryUndirectedGraph(s)
        return factory
    G.multicutIlpGlpkFactory = staticmethod(multicutIlpGlpkFactory)
    O.multicutIlpGlpkFactory = staticmethod(multicutIlpGlpkFactory)

    def multicutIlpFactory( ilpSolver = 'cplex',
                            verbose=0, addThreeCyclesConstraints=True,
                            addOnlyViolatedThreeCyclesConstraints=True,
                            relativeGap=0.0, absoluteGap=0.0, memLimit=-1.0):
        
        if ilpSolver == 'cplex':
            f = multicutIlpCplexFactory
        elif ilpSolver == 'gurobi':
            f = multicutIlpGurobiFactory
        elif ilpSolver == 'glpk':
            f = multicutIlpGlpkFactory
        elif ilpSolver == 'coin-cbc' or ilpSolver == 'cbc':
            f = multicutIlpCoinCbcFactory
        else:
            raise RuntimeError("%s is an unknown ilp solver"%str(ilpSolver))
        return f(verbose=verbose,addThreeCyclesConstraints=addThreeCyclesConstraints,
                addOnlyViolatedThreeCyclesConstraints=addOnlyViolatedThreeCyclesConstraints,
                relativeGap=relativeGap, absoluteGap=absoluteGap, memLimit=memLimit)
    G.multicutIlpFactory = staticmethod(multicutIlpFactory)
    O.multicutIlpFactory = staticmethod(multicutIlpFactory)

    def fusionMoveSettings(mcFactory=greedyAdditiveFactory()):
        s = graph.multicut.FusionMoveSettingsUndirectedGraph()
        s.mcFactory = mcFactory
        return s
    G.fusionMoveSettings = staticmethod(fusionMoveSettings)
    O.fusionMoveSettings = staticmethod(fusionMoveSettings)

    def fusionMoveBasedFactory(numberOfIterations=10,verbose=0,
                               numberOfParallelProposals=10, fuseN=2,
                               stopIfNoImprovement=4,
                               numberOfThreads=-1,
                               proposalGen=greedyAdditiveProposals(),
                               fusionMove=fusionMoveSettings()):
        solverSettings = None
        if isinstance(proposalGen, graph.multicut.FusionMoveBasedGreedyAdditiveProposalGenSettingsUndirectedGraph):
            solverSettings = graph.multicut.FusionMoveBasedGreedyAdditiveSettingsUndirectedGraph()
            factoryCls = graph.multicut.FusionMoveBasedGreedyAdditiveFactoryUndirectedGraph
        elif isinstance(proposalGen, graph.multicut.FusionMoveBasedWatershedProposalGenSettingsUndirectedGraph):
            solverSettings = graph.multicut.FusionMoveBasedWatershedSettingsUndirectedGraph()
            factoryCls = graph.multicut.FusionMoveBasedWatershedFactoryUndirectedGraph
        else:
            raise TypeError(str(proposalGen)+" is of unknown type")

        solverSettings.fusionMoveSettings = fusionMove
        solverSettings.proposalGenSettings = proposalGen
        solverSettings.numberOfIterations = int(numberOfIterations)
        solverSettings.verbose = int(verbose)
        solverSettings.numberOfParallelProposals = int(numberOfParallelProposals)
        solverSettings.fuseN = int(fuseN)
        solverSettings.stopIfNoImprovement = int(stopIfNoImprovement)
        solverSettings.numberOfThreads = int(numberOfThreads)
        factory = factoryCls(solverSettings)
        return factory
    G.fusionMoveBasedFactory = staticmethod(fusionMoveBasedFactory)
    O.fusionMoveBasedFactory = staticmethod(fusionMoveBasedFactory)



    def perturbAndMapSettings(mcFactory):
        s = graph.multicut.PerturbAndMapSettingsUndirectedGraph()
        s.mcFactory = mcFactory
        return s
    G.perturbAndMapSettings = staticmethod(perturbAndMapSettings)
    O.perturbAndMapSettings = staticmethod(perturbAndMapSettings)

    def perturbAndMap(objective, settings):
        pAndM = graph.multicut.perturbAndMap(objective, settings)
        return pAndM
    G.perturbAndMap = staticmethod(perturbAndMap)
    O.perturbAndMap = staticmethod(perturbAndMap)

__addStaticMethodsToUndirectedGraphAndMulticutObjectiveUndirectedGraph()
del __addStaticMethodsToUndirectedGraphAndMulticutObjectiveUndirectedGraph