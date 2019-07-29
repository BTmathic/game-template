from equipment_slots import EquipmentSlots


class Equipment:
    def __init__(
            self,
            main_hand=None,
            off_hand=None,
            head=None,
            body=None,
            legs=None,
            boots=None,
            l_ring=None,
            r_ring=None,
            cloak=None
    ):
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.head = head
        self.body = body
        self.legs = legs
        self.boots = boots
        self.l_ring = l_ring
        self.r_ring = r_ring
        self.cloak = cloak

    @property
    def max_hp_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_hp_bonus
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_hp_bonus
        if self.head and self.head.equippable:
            bonus += self.head.equippable.max_hp_bonus
        if self.body and self.body.equippable:
            bonus += self.body.equippable.max_hp_bonus
        if self.legs and self.legs.equippable:
            bonus += self.legs.equippable.max_hp_bonus
        if self.boots and self.boots.equippable:
            bonus += self.boots.equippable.max_hp_bonus
        if self.l_ring and self.l_ring.equippable:
            bonus += self.l_ring.equippable.max_hp_bonus
        if self.r_ring and self.r_ring.equippable:
            bonus += self.r_ring.equippable.max_hp_bonus
        if self.cloak and self.cloak.equippable:
            bonus += self.cloak.equippable.max_hp_bonus

        return bonus

    @property
    def power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.power_bonus
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.power_bonus
        if self.head and self.head.equippable:
            bonus += self.head.equippable.power_bonus
        if self.body and self.body.equippable:
            bonus += self.body.equippable.power_bonus
        if self.legs and self.legs.equippable:
            bonus += self.legs.equippable.power_bonus
        if self.boots and self.boots.equippable:
            bonus += self.boots.equippable.power_bonus
        if self.l_ring and self.l_ring.equippable:
            bonus += self.l_ring.equippable.power_bonus
        if self.r_ring and self.r_ring.equippable:
            bonus += self.r_ring.equippable.power_bonus
        if self.cloak and self.cloak.equippable:
            bonus += self.cloak.equippable.power_bonus

        return bonus

    @property
    def defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.defense_bonus
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.defense_bonus
        if self.head and self.head.equippable:
            bonus += self.head.equippable.defense_bonus
        if self.body and self.body.equippable:
            bonus += self.body.equippable.defense_bonus
        if self.legs and self.legs.equippable:
            bonus += self.legs.equippable.defense_bonus
        if self.boots and self.boots.equippable:
            bonus += self.boots.equippable.defense_bonus
        if self.l_ring and self.l_ring.equippable:
            bonus += self.l_ring.equippable.defense_bonus
        if self.r_ring and self.r_ring.equippable:
            bonus += self.r_ring.equippable.defense_bonus
        if self.cloak and self.cloak.equippable:
            bonus += self.cloak.equippable.defense_bonus

        return bonus

    def toggle_equip(self, equippable_entity):
        results = []

        slot = equippable_entity.equippable.slot
        if slot == EquipmentSlots.MAIN_HAND:
            if self.main_hand == equippable_entity:
                self.main_hand = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.main_hand:
                    results.append({'unequipped': self.main_hand})
                self.main_hand = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.OFF_HAND:
            if self.off_hand == equippable_entity:
                self.off_hand = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.off_hand:
                    results.append({'unequipped': self.off_hand})
                self.off_hand = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.HEAD:
            if self.head == equippable_entity:
                self.head = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.head:
                    results.append({'unequipped': self.head})
                self.head = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.BODY:
            if self.body == equippable_entity:
                self.body = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.body:
                    results.append({'unequipped': self.body})
                self.body = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.LEGS:
            if self.legs == equippable_entity:
                self.legs = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.legs:
                    results.append({'unequipped': self.legs})
                self.legs = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.BOOTS:
            if self.boots == equippable_entity:
                self.boots = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.boots:
                    results.append({'unequipped': self.boots})
                self.boots = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.L_RING:
            if self.l_ring == equippable_entity:
                self.l_ring = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.l_ring:
                    results.append({'unequipped': self.l_ring})
                self.l_ring = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.R_RING:
            if self.r_ring == equippable_entity:
                self.r_ring = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.r_ring:
                    results.append({'unequipped': self.r_ring})
                self.r_ring = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.CLOAK:
            if self.cloak == equippable_entity:
                self.cloak = None
                results.append({'unequipped': equippable_entity})
            else:
                if self.cloak:
                    results.append({'unequipped': self.cloak})
                self.cloak = equippable_entity
                results.append({'equipped': equippable_entity})

        return results
