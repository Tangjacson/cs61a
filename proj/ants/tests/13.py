test = {
  'name': 'Problem 13',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'answer': '80f6dfebbb21c78163b8aa9dc8abbe28',
          'choices': [
            'ScubaThrower',
            'Ant',
            'Insect',
            'AntColony'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What class does QueenAnt inherit from?'
        },
        {
          'answer': 'ec203a8bd48f4369ee6fc9a03ffdbfcc',
          'choices': [
            'The first QueenAnt that is instantiated',
            'The second QueenAnt that is instantiated',
            'The most recent QueenAnt that is instantiated',
            'All QueenAnt instances are true QueenAnts'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Which QueenAnt instance is the true QueenAnt?'
        },
        {
          'answer': '5b60299a3505c6a816e3f5d6d44fa408',
          'choices': [
            'Its armor is reduced to 0 upon taking its first action',
            'Nothing, the game ends',
            'The armor of the first QueenAnt is reduced to 0',
            'It doubles the damage of all the ants behind it'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What happens to any QueenAnt instance that is instantiated after the
          first one?
          """
        },
        {
          'answer': '7f1e876193ad01466bb1f843c9a17b72',
          'choices': [
            r"""
            Attacks the nearest bee and doubles the damage of all the ants
            behind her (that haven't already been doubled)
            """,
            r"""
            Doubles the damage of all the ants behind her (that haven't
            already been doubled)
            """,
            r"""
            Doubles the damage of all the ants in front of her (that haven't
            already been doubled)
            """,
            r"""
            Doubles the damage of all the ants in the colony (that haven't
            already been doubled)
            """
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does the true QueenAnt do each turn?'
        },
        {
          'answer': 'a753f5e0cf5cd82c878a589f863e2e48',
          'choices': [
            'If a Bee reaches the end of a tunnel or the true QueenAnt dies',
            'If there are no ants left in the colony',
            'If an imposter QueenAnt is placed in the colony',
            'If a Bee attacks the true QueenAnt'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Under what circumstances do Bees win the game?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing QueenAnt parameters
          >>> QueenAnt.food_cost
          7cd035adf49fc93a635b4e8bb2e28bd4
          # locked
          >>> queen = QueenAnt()
          >>> queen.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # QueenAnt Placement
          >>> queen = ants.QueenAnt()
          >>> impostor = ants.QueenAnt()
          >>> front_ant, back_ant = ants.ThrowerAnt(), ants.ThrowerAnt()
          >>> tunnel = [colony.places['tunnel_0_{0}'.format(i)]
          ...         for i in range(9)]
          >>> tunnel[1].add_insect(back_ant)
          >>> tunnel[7].add_insect(front_ant)
          >>> tunnel[4].add_insect(impostor)
          >>> impostor.action(colony)
          >>> impostor.armor            # Impostors must die!
          0
          >>> tunnel[4].ant is None
          True
          >>> back_ant.damage           # Ants should not be buffed
          1
          >>> front_ant.damage
          1
          >>> tunnel[4].add_insect(queen)
          >>> queen.action(colony)
          >>> queen.armor               # Long live the Queen!
          1
          >>> back_ant.damage           # Ants behind queen should be buffed
          2
          >>> front_ant.damage
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # QueenAnt Removal
          >>> queen = ants.QueenAnt()
          >>> impostor = ants.QueenAnt()
          >>> place = colony.places['tunnel_0_2']
          >>> place.add_insect(impostor)
          >>> place.remove_insect(impostor)
          >>> place.ant is None         # Impostors can be removed
          True
          >>> place.add_insect(queen)
          >>> place.remove_insect(queen)
          >>> place.ant is queen        # True queen cannot be removed
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # QueenAnt knows how to swim
          >>> queen = ants.QueenAnt()
          >>> water = ants.Water('Water')
          >>> water.add_insect(queen)
          >>> queen.armor
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing damage multiplier
          >>> queen_tunnel, side_tunnel = [[colony.places['tunnel_{0}_{1}'.format(i, j)]
          ...         for j in range(9)] for i in range(2)]
          >>> # layout
          >>> # queen_tunnel: [Back, Guard/Guarded, Queen, Front, Bee     ]
          >>> # side_tunnel : [Side,              ,      ,      , Side Bee]
          >>> queen = ants.QueenAnt()
          >>> back = ants.ThrowerAnt()
          >>> front = ants.ThrowerAnt()
          >>> guard = ants.BodyguardAnt()
          >>> guarded = ants.ThrowerAnt()
          >>> side = ants.ThrowerAnt()
          >>> bee = ants.Bee(10)
          >>> side_bee = ants.Bee(10)
          >>> queen_tunnel[0].add_insect(back)
          >>> queen_tunnel[1].add_insect(guard)
          >>> queen_tunnel[1].add_insect(guarded)
          >>> queen_tunnel[2].add_insect(queen)
          >>> queen_tunnel[3].add_insect(front)
          >>> side_tunnel[0].add_insect(side)
          >>> queen_tunnel[4].add_insect(bee)
          >>> side_tunnel[4].add_insect(side_bee)
          >>> queen.action(colony)
          >>> bee.armor
          9
          >>> back.action(colony)
          >>> bee.armor
          7
          >>> front.action(colony)
          >>> bee.armor
          6
          >>> guard.action(colony)
          >>> bee.armor
          4
          >>> side.action(colony)
          >>> side_bee.armor
          9
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import ants, importlib
      >>> importlib.reload(ants)
      >>> beehive = ants.Hive(ants.AssaultPlan())
      >>> dimensions = (2, 9)
      >>> colony = ants.AntColony(None, beehive, ants.ant_types(),
      ...         ants.dry_layout, dimensions)
      >>> ants.bees_win = lambda: None
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing game over
          >>> queen = ants.QueenAnt()
          >>> impostor = ants.QueenAnt()
          >>> tunnel = [colony.places['tunnel_0_{0}'.format(i)]
          ...         for i in range(9)]
          >>> tunnel[4].add_insect(queen)
          >>> tunnel[6].add_insect(impostor)
          >>> bee = ants.Bee(3)
          >>> tunnel[6].add_insect(bee)     # Bee in place with impostor
          >>> bee.action(colony)            # Game should not end
          
          >>> bee.move_to(tunnel[4])        # Bee moved to place with true queen
          >>> bee.action(colony)            # Game should end
          BeesWinException
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing if queen will not crash with no one to buff
          >>> queen = ants.QueenAnt()
          >>> colony.places['tunnel_0_2'].add_insect(queen)
          >>> queen.action(colony)
          >>> # Attack a bee
          >>> bee = ants.Bee(3)
          >>> colony.places['tunnel_0_4'].add_insect(bee)
          >>> queen.action(colony)
          >>> bee.armor # Queen should still hit the bee
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing QueenAnt action method
          >>> queen = ants.QueenAnt()
          >>> impostor = ants.QueenAnt()
          >>> bee = ants.Bee(10)
          >>> ant = ants.ThrowerAnt()
          >>> colony.places['tunnel_0_0'].add_insect(ant)
          >>> colony.places['tunnel_0_1'].add_insect(queen)
          >>> colony.places['tunnel_0_2'].add_insect(impostor)
          >>> colony.places['tunnel_0_4'].add_insect(bee)
          
          >>> impostor.action(colony)
          >>> bee.armor   # Impostor should not damage bee
          10
          >>> ant.damage  # Impostor should not double damage
          1
          
          >>> queen.action(colony)
          >>> bee.armor   # Queen should damage bee
          9
          >>> ant.damage  # Queen should double damage
          2
          >>> ant.action(colony)
          >>> bee.armor   # If failed, ThrowerAnt has incorrect damage
          7
          
          >>> queen.armor   # Long live the Queen
          1
          >>> impostor.armor  # Short-lived impostor
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Extensive damage doubling tests
          >>> queen_tunnel, side_tunnel = [[colony.places['tunnel_{0}_{1}'.format(i, j)]
          ...         for j in range(9)] for i in range(2)]
          >>> queen = ants.QueenAnt()
          >>> queen_tunnel[7].add_insect(queen)
          >>> # Turn 0
          >>> thrower = ants.ThrowerAnt()
          >>> fire = ants.FireAnt()
          >>> ninja = ants.NinjaAnt()
          >>> side = ants.ThrowerAnt()
          >>> front = ants.NinjaAnt()
          >>> queen_tunnel[0].add_insect(thrower)
          >>> queen_tunnel[1].add_insect(fire)
          >>> queen_tunnel[2].add_insect(ninja)
          >>> queen_tunnel[8].add_insect(front)
          >>> side_tunnel[0].add_insect(side)
          >>> # layout right now
          >>> # [thrower, fire, ninja, , , , , queen, front]
          >>> # [side   ,     ,      , , , , ,      ,      ]
          >>> thrower.damage, fire.damage, ninja.damage = 101, 102, 103
          >>> front.damage, side.damage = 104, 105
          >>> queen.action(colony)
          >>> (thrower.damage, fire.damage, ninja.damage)
          (202, 204, 206)
          >>> (front.damage, side.damage)
          (104, 105)
          >>> # Turn 1
          >>> tank = ants.TankAnt()
          >>> guard = ants.BodyguardAnt()
          >>> queen_tank = ants.TankAnt()
          >>> queen_tunnel[6].add_insect(tank)          # Not protecting an ant
          >>> queen_tunnel[1].add_insect(guard)         # Guarding FireAnt
          >>> queen_tunnel[7].add_insect(queen_tank)    # Guarding QueenAnt
          >>> # layout right now
          >>> # [thrower, guard/fire, ninja, , , , tank, queen_tank/queen, front]
          >>> # [side   ,           ,      , , , ,     ,                 ,      ]
          >>> tank.damage, guard.damage, queen_tank.damage = 1001, 1002, 1003
          >>> queen.action(colony)
          >>> # unchanged
          >>> (thrower.damage, fire.damage, ninja.damage)
          (202, 204, 206)
          >>> (front.damage, side.damage)
          (104, 105)
          >>> (tank.damage, guard.damage)
          (2002, 2004)
          >>> queen_tank.damage
          1003
          >>> # Turn 2
          >>> thrower1 = ants.ThrowerAnt()
          >>> thrower2 = ants.ThrowerAnt()
          >>> queen_tunnel[6].add_insect(thrower1)      # Add thrower1 in TankAnt
          >>> queen_tunnel[5].add_insect(thrower2)
          >>> # layout right now
          >>> # [thrower, guard/fire, ninja, , , thrower2, tank/thrower1, queen_tank/queen, front]
          >>> # [side   ,           ,      , , ,         ,              ,                 ,      ]
          >>> thrower1.damage, thrower2.damage = 10001, 10002
          >>> queen.action(colony)
          >>> (thrower.damage, fire.damage, ninja.damage)
          (202, 204, 206)
          >>> (front.damage, side.damage)
          (104, 105)
          >>> (tank.damage, guard.damage)
          (2002, 2004)
          >>> queen_tank.damage
          1003
          >>> (thrower1.damage, thrower2.damage)
          (20002, 20004)
          >>> # Turn 3
          >>> tank.reduce_armor(tank.armor)             # Expose thrower1
          >>> queen.action(colony)
          >>> (thrower.damage, fire.damage, ninja.damage)
          (202, 204, 206)
          >>> (front.damage, side.damage)
          (104, 105)
          >>> guard.damage
          2004
          >>> queen_tank.damage
          1003
          >>> (thrower1.damage, thrower2.damage)
          (20002, 20004)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Adding/Removing QueenAnt with Container
          >>> place = colony.places['tunnel_0_3']
          >>> queen = ants.QueenAnt()
          >>> impostor = ants.QueenAnt()
          >>> container = ants.TankAnt()
          >>> place.add_insect(container)
          >>> place.add_insect(impostor)
          >>> impostor.action(colony)
          >>> place.ant is container
          True
          >>> container.place is place
          True
          >>> container.contained_ant is None
          True
          >>> impostor.place is None
          True
          >>> place.add_insect(queen)
          >>> place.remove_insect(queen)
          >>> container.contained_ant is queen
          True
          >>> queen.place is place
          True
          >>> queen.action(colony) # should not error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # test proper call to death callback
          >>> original_death_callback = ants.Insect.death_callback
          >>> ants.Insect.death_callback = lambda x: print("insect died")
          >>> real = ants.QueenAnt()
          >>> impostor = ants.QueenAnt()
          >>> colony.places['tunnel_0_2'].add_insect(real)
          >>> colony.places['tunnel_0_3'].add_insect(impostor)
          >>> impostor.action(colony)
          insect died
          >>> ants.Insect.death_callback = original_death_callback
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import ants, importlib
      >>> importlib.reload(ants)
      >>> beehive = ants.Hive(ants.AssaultPlan())
      >>> dimensions = (2, 9)
      >>> colony = ants.AntColony(None, beehive, ants.ant_types(),
      ...         ants.dry_layout, dimensions)
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
