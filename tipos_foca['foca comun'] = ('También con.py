tipos_foca = {}
tipos_foca['foca comun'] = ('También conocida como foca del puerto, es una especie ampliamente distribuida en aguas costeras del Atlántico y el Pacífico.')
tipos_foca['foca de wedell'] = ('Su pelaje es gris oscuro o marrón, y pueden alcanzar hasta 3 metros de longitud.')
tipos_foca['foca anillada'] = ('Son conocidas por ser buenas nadadoras y pueden permanecer sumergidas durante largos períodos de tiempo.')
tipos_foca['foca leoparda'] = ('Es una depredadora ágil y versátil, cazando una variedad de presas marinas, incluidos pingüinos y otras focas.')
tipos_foca['foca barbuda'] = ('Su nombre deriva de las largas vibrisas o "barbas" en su rostro.')
tipos_foca['Foca de Ross '] = ('Se alimentan principalmente de peces y cefalópodos.')
tipos_foca['Foca monje del Mediterráneo'] = ('Es una especie en peligro crítico de extinción y es una de las focas más raras del mundo')
tipos_foca['Foca de la Antártida '] = ('Se alimentan principalmente de krill y peces.')
tipos_foca['Foca de crin'] = ('También conocida como foca de lobo o foca de melena, habita en las costas rocosas y las plataformas de hielo del Atlántico norte.')
tipos_foca['Foca de la isla de Saimaa'] = ('Es una subespecie en peligro crítico de extinción y es endémica de la región de los lagos de Saimaa en Finlandia.')

while True:
    menu = int(input('1 MOSTRAR TODAS LAS FOCAS. 2 ELIMINAR FOCAS. 3 AGREGAR FOCAS. 4 MODIFICAR FOCAS'))
    
    if menu == 1:
        print(tipos_foca)
        
        
    elif menu == 2:
        remover = input('¿que foca quieres remover?')
        tipos_foca[remover] = ''
        
        
    elif menu == 3:
        agregar = input('¿que foca quieres agregar?')
        descripcion = input("¿Que informacion agregaras de la foca",agregar," ?")
        tipos_foca[agregar]  = descripcion
        print('se a agregado la foca', agregar)

        
        
    else:
        modificar = input('¿que foca quieres modificar?')
        descripcion =input('queonformacion editaras de la foca?:')
        
        tipos_foca[modificar] = descripcion