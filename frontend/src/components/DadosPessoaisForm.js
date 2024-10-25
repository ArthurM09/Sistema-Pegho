import React, { useState } from 'react';
import api from '../api';

const DadosPessoaisForm = () => {
    const [nome, setNome] = useState('');
    const [dataNascimento, setDataNascimento] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const dados = { nome, data_nascimento: dataNascimento };
        try {
            await api.post('/dadospessoais/', dados);
            alert('Dados pessoais salvos com sucesso!');
        } catch (error) {
            console.error("Erro ao salvar dados pessoais", error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Nome:
                <input type="text" value={nome} onChange={(e) => setNome(e.target.value)} />
            </label>
            <label>
                Data de Nascimento:
                <input type="date" value={dataNascimento} onChange={(e) => setDataNascimento(e.target.value)} />
            </label>
            <button type="submit">Enviar</button>
        </form>
    );
};

export default DadosPessoaisForm;
