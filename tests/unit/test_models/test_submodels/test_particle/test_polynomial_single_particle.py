#
# Test single polynomial particles
#

import pybamm
import tests
import unittest


class TestSingleParticle(unittest.TestCase):
    def test_public_functions(self):
        param = pybamm.LithiumIonParameters()

        a = pybamm.PrimaryBroadcast(pybamm.Scalar(0), "current collector")

        variables = {
            "Current collector current density": a,
            "X-averaged negative electrode interfacial current density": a,
            "X-averaged negative electrode temperature": a,
        }

        submodel = pybamm.particle.PolynomialSingleParticle(param, "Negative", order=0)
        std_tests = tests.StandardSubModelTests(submodel, variables)
        std_tests.test_all()

        submodel = pybamm.particle.PolynomialSingleParticle(param, "Negative", order=2)
        std_tests = tests.StandardSubModelTests(submodel, variables)
        std_tests.test_all()

        submodel = pybamm.particle.PolynomialSingleParticle(param, "Negative", order=4)
        std_tests = tests.StandardSubModelTests(submodel, variables)
        std_tests.test_all()

        variables = {
            "Current collector current density": a,
            "X-averaged positive electrode interfacial current density": a,
            "X-averaged positive electrode temperature": a,
        }

        submodel = pybamm.particle.PolynomialSingleParticle(param, "Positive", order=0)
        std_tests = tests.StandardSubModelTests(submodel, variables)
        std_tests.test_all()

        submodel = pybamm.particle.PolynomialSingleParticle(param, "Positive", order=2)
        std_tests = tests.StandardSubModelTests(submodel, variables)
        std_tests.test_all()

        submodel = pybamm.particle.PolynomialSingleParticle(param, "Positive", order=4)
        std_tests = tests.StandardSubModelTests(submodel, variables)
        std_tests.test_all()


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    pybamm.settings.debug_mode = True
    unittest.main()