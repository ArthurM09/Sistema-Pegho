import React, { useState } from 'react';
import api from '../api';

const ExperienciaProfissionalForm = () => {
    const [cargo, setCargo] = useState('');
    const [empresa, setEmpresa] = useState('');
    const [inicio, setInicio] = useState('');
    const [fim, setFim] = useState('');
    const [descricao, setDescricao] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const dados = { cargo, empresa, inicio, fim, descricao };
        try {
            await api.post('/experienciaprofissional/', dados);
            alert('Experiência profissional salva com sucesso!');
        } catch (error) {
            console.error("Erro ao salvar experiência profissional", error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Cargo:
                <input type="text" value={cargo} onChange={(e) => setCargo(e.target.value)} />
            </label>
            <label>
                Empresa:
                <input type="date" value={empresa} onChange={(e) => setEmpresa(e.target.value)} />
            </label>
            <label>
                Data de entrada:
                <input type="date" value={inicio} onChange={(e) => setInicio(e.target.value)} />
            </label>
            <label>
                Data de saída:
                <input type="date" value={fim} onChange={(e) => setFim(e.target.value)} />
            </label>
            <label>
                Descrição:
                <input type="date" value={descricao} onChange={(e) => setDescricao(e.target.value)} />
            </label>
            <button type="submit">Enviar</button>
        </form>
    );
};

export default ExperienciaProfissionalForm;
