

from pyboolnet.file_exchange import bnet2primes, primes2bnet
from pyboolnet.prime_implicants import *
from pyboolnet.repository import *
from pyboolnet.state_transition_graphs import *

from pyboolnet.model_checking import *
from pyboolnet.attractors import *
from pyboolnet.interaction_graphs import *


if __name__ == "__main__":
    bnet = """
    v1,    !v1
    v2,    1
    v3,    v2 & (!v1 | v3)
    """

    repre = """
    v1, !v3
    v2, !v1
    v3, !v2
    """

    #init represilatorja
    primes_repre = bnet2primes(repre)

    #init bnet exampla 
    primes_bnet = bnet2primes(bnet)

    # ================= finding nodes =================

    # iskane konstant v represilatorju
    print("Konstante v represilatorju:")
    const_repre = find_constants(primes_repre)
    print(const_repre)

    # iskane konstant v bnet examplu 
    print("Konstante v bnet examplu:")
    const_bnet = find_constants(primes_bnet)
    print(const_bnet)

    # ================= modifying networks =================

    create_variables(primes_bnet, {"v4": "v4 | v2"})
    
    # dodajanje spremenljivke z lambda funkcijo (nevem čist kako dela)
    # create_variables(primes, {"v5": lambda v1, v2, v3: v1 + v2 + v3 == 1})

    # Izpis omrežja
    print("Novo bnet omrežje:")
    print(primes2bnet(primes_bnet)) 

    # ================= Izris grafov =================

    # Izris grafa za represilator
    create_stg_image(primes_repre, update="asynchronous", fname_image="igraph.pdf")
    create_stg_image(primes_repre, update="asynchronous", fname_image="igraph2.pdf", styles=["anonymous", "sccs"])

    #TODO a so grafi drugačni če jih

    # Izris grafa za bnet
    create_stg_image(primes_bnet, update="asynchronous", fname_image="igraph.pdf")
    create_stg_image(primes_bnet, update="asynchronous", fname_image="igraph2.pdf", styles=["anonymous", "sccs"])


    # ================= Računanje attraktorjev =================

    stg_repre_sync = primes2stg(primes_repre, update="synchronous")

    stg_repre_async = primes2stg(primes_repre, update="asynchronous")

    steady_async, ciklicna_async = compute_attractors_tarjan(stg_repre_async)

    steady_sync, ciklicna_sync = compute_attractors_tarjan(stg_repre_sync)

    #izpis
    print("================= Izpis attraktorjev =================")
    print("steady async")
    print(steady_async)  

    print("ciklicna async")
    print(ciklicna_async)

    print("steady sync")
    print(steady_sync)

    print("ciklicna sync")
    print(ciklicna_sync)

    # random walk za represilator (ne dela neki)

    # stanje_repre = find_attractor_state_by_randomwalk_and_ctl(primes_repre, "asynchronous")

    # print("Stanje represilatorja:")
    # print(stanje_repre)

    # attraktorji na nek drug more different way (isto še ne dela neki idk man)

    # atrktorji_repre = compute_attractors(primes_repre, update="asynchronous", fname_json="attractors.json")

    # print("Attraktorji represilatorja:")
    # print(atrktorji_repre["is_complete"])
    # for x in atrktorji_repre["attractors"]:
    #     print(x["is_steady"])
    #     print(x["state"]["str"])