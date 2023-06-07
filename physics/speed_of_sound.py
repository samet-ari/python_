"""
Title : Calculating the speed of sound

Description :
    The speed of sound (c) is the speed that a sound wave travels
    per unit time (m/s). During propagation, the sound wave propagates
    through an elastic medium. Its SI unit is meter per second (m/s).

    Only longitudinal waves can propagate in liquids and gas other then
    solid where they also travel in  transverse wave. The following Algo-
    rithem calculates the speed of sound in fluid depanding on the bulk
    module and the density of the fluid.

    Equation for calculating speed od sound in fluid:
    c_fluid = (K_s*p)**0.5

    c_fluid: speed of sound in fluid
    K_s: isentropic bulk modulus
    p: density of fluid



Source : https://en.wikipedia.org/wiki/Speed_of_sound
"""


class SpeedOfSound:
    @staticmethod
    def fluid(fluid_density: float, bulk_modulus: float) -> float:
        """
        This method calculates the speed of sound in fluid -
        This is calculated from the other two provided values
        Examples:
        Example 1 --> Water 20°C: bulk_moduls= 2.15MPa, fluid_density=998kg/m³
        Example 2 --> Murcery 20°: bulk_moduls= 28.5MPa, fluid_density=13600kg/m³

        >>> SpeedOfSound.fluid(bulk_modulus=2.15*10**9, fluid_density=998)
        1467.7563207952705
        >>> SpeedOfSound.fluid(bulk_modulus=28.5*10**9, fluid_density=13600)
        1447.614670861731
        """

        if fluid_density <= 0:
            raise ValueError("Impossible fluid density")
        if bulk_modulus <= 0:
            raise ValueError("Impossible bulk modulus")

        speed_of_sound = (bulk_modulus / fluid_density) ** 0.5

        return speed_of_sound


if __name__ == "__main__":
    import doctest

    doctest.testmod()
